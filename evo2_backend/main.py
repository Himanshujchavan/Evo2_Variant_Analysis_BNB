import sys
import modal

from evo2.genome_utils import get_genome_sequence
from evo2.analyzer import analyze_variant
from evo2.constants import WINDOW_SIZE

evo2_image = (
    modal.Image.from_registry(
        "nvidia/cuda:12.4.0-devel-ubuntu22.04", add_python="3.12"
    )
    .apt_install([
        "build-essential", "cmake", "ninja-build",
        "libcudnn8", "libcudnn8-dev", "git", "clang", "gcc", "g++"
    ])
    .env({
        "CC": "/usr/bin/gcc",
        "CXX": "/usr/bin/g++",
    })
    .run_commands("git clone --recurse-submodules https://github.com/ArcInstitute/evo2.git && cd evo2 && pip install .")
    .run_commands("sed -i \"s/np.fromstring(text, dtype=np.uint8)/np.frombuffer(text.encode(), dtype=np.uint8)/g\" evo2/vortex/vortex/model/tokenizer.py")
    .run_commands("pip uninstall -y transformer-engine transformer_engine")
    .run_commands("pip install 'transformer_engine[pytorch]==1.13' --no-build-isolation")
    .pip_install("fastapi[standard]")
    .pip_install_from_requirements("requirements.txt")
)

app = modal.App("variant-analysis-evo2-BNB", image=evo2_image)

volume = modal.Volume.from_name("hf_cache", create_if_missing=True)
mount_path = "/root/.cache/huggingface"

@app.cls(gpu="H100", volumes={mount_path: volume}, max_containers=3, retries=2, scaledown_window=120)
class Evo2Model:
    @modal.enter()
    def load_model(self):
        from evo2 import Evo2
        print("Loading Evo2 model...")
        self.model = Evo2("evo2_7b")
        print("Evo2 model loaded.")

    @modal.fastapi_endpoint(method="POST")
    def analyze_single_variant(self, variant_position: int, alternative: str, genome: str, chromosome: str):
        print("Received Variant:")
        print(f"  Genome: {genome}")
        print(f"  Chromosome: {chromosome}")
        print(f"  Position: {variant_position}")
        print(f"  Alternative: {alternative}")

        window_seq, seq_start = get_genome_sequence(
            position=variant_position,
            genome=genome,
            chromosome=chromosome,
            window_size=WINDOW_SIZE
        )

        relative_pos = variant_position - 1 - seq_start
        if relative_pos < 0 or relative_pos >= len(window_seq):
            raise ValueError(
                f"Variant position {variant_position} is outside the fetched window (start={seq_start + 1}, end={seq_start + len(window_seq)})"
            )

        reference = window_seq[relative_pos]
        print(f"Reference base at position: {reference}")

        result = analyze_variant(
            relative_pos_in_window=relative_pos,
            reference=reference,
            alternative=alternative,
            window_seq=window_seq,
            model=self.model
        )

        result["position"] = variant_position
        return result

@app.local_entrypoint()
def main():
    # Example for local test (only runs if you do modal run main.py)
    evo2_model = Evo2Model()
    result = evo2_model.analyze_single_variant.remote(
        variant_position=43119628,
        alternative="G",
        genome="hg38",
        chromosome="chr17"
    )
    print("Inference Result:")
    print(result)
