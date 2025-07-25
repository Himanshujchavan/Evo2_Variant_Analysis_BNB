# Evo2 Variant Analysis Platform

A comprehensive genomic variant analysis platform built on Binance Smart Chain (BSC) that combines blockchain technology with advanced genomic analysis. The platform includes NFT-based genomic data ownership, a marketplace for genomic data trading, DAO governance, and AI-powered variant analysis.

## ⚡ Quick Run Locally (TL;DR)

**Just want to run it? Follow these 4 simple steps:**

```bash
# 1. Clone and install frontend
git clone https://github.com/PratikRai0101/Evo2_Variant_Analysis_BNB.git
cd Evo2_Variant_Analysis_BNB/evo2_frontend
npm install

# 2. Copy the .env file (already configured with deployed contracts)
# The .env file is already set up with working contract addresses!

# 3. Start frontend
npm run dev

# 4. In a new terminal, start backend
cd ../evo2_backend
pip install -r requirements.txt
python start_api.py
```

**That's it!** 🎉
- Frontend: `http://localhost:3000`
- Backend: `http://localhost:8000`
- Connect MetaMask to BSC Testnet (Chain ID: 97)
- Get test BNB from [BSC Faucet](https://testnet.bnbchain.org/faucet-smart)

---

## 🏗️ Architecture

- **Frontend**: Next.js 14 with TypeScript, TailwindCSS, and Web3 integration
- **Backend**: Python FastAPI with Modal.com integration for scalable analysis
- **Blockchain**: Smart contracts deployed on BSC Testnet
- **Analysis**: AI-powered genomic variant analysis through Modal.com

## 📋 Prerequisites

- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **Git**
- **MetaMask** or compatible Web3 wallet
- **BSC Testnet** BNB for testing (get from [BSC Testnet Faucet](https://testnet.bnbchain.org/faucet-smart))

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/PratikRai0101/Evo2_Variant_Analysis_BNB.git
cd Evo2_Variant_Analysis_BNB
```

### 2. Setup Frontend

```bash
cd evo2_frontend
npm install
```

Create `.env` file in `evo2_frontend/` directory:
```env
NEXT_PUBLIC_ANALYZE_SINGLE_VARIANT_BASE_URL=https://pratikrai0101--variant-analysis-evo2-bnb-evo2model-analy-f8e3c9.modal.run/

# Blockchain Contract Addresses (BSC Testnet)
NEXT_PUBLIC_GENOME_NFT_ADDRESS=0x2181B366B730628F97c44C17de19949e5359682C
NEXT_PUBLIC_GENOME_TOKEN_ADDRESS=0x0C5f98e281cB3562a2EEDF3EE63D3b623De98b15
NEXT_PUBLIC_MARKETPLACE_ADDRESS=0xd80bE0DDCA595fFf35bF44A7d2D4E312b05A1576
NEXT_PUBLIC_DAO_ADDRESS=0x8FEbF8eA03E8e54846a7B82f7F6146bAE17bd3f4

# Optional: API and Chain Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_CHAIN_ID=97
```

Start the frontend:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

### 3. Setup Backend

```bash
cd ../evo2_backend
pip install -r requirements.txt
```

Start the backend server:
```bash
python start_api.py
```

The backend API will be available at `http://localhost:8000`

### 4. Setup Blockchain (Optional - for development)

If you want to deploy your own contracts:

```bash
cd ../contracts
npm install
```

Create `.env` file in `contracts/` directory:
```env
PRIVATE_KEY=your_private_key_here
BSC_TESTNET_RPC_URL=https://data-seed-prebsc-1-s1.bnbchain.org:8545
```

Deploy contracts:
```bash
npx hardhat run scripts/deploy-full-platform.js --network bscTestnet
```

## 🧬 Features

### 1. Genomic Variant Analysis
- Upload genomic sequences for analysis
- AI-powered variant detection and classification
- BRCA1 gene analysis with pathogenicity prediction
- Interactive visualization of variants

### 2. NFT-Based Genomic Data Ownership
- Mint genomic data as NFTs
- Secure ownership and provenance tracking
- Metadata storage with IPFS integration

### 3. Genomic Data Marketplace
- List genomic data for sale or licensing
- Purchase data with BNB or Genome Tokens
- Flexible access levels and duration

### 4. DAO Governance
- Community-driven decision making
- Proposal creation and voting
- Genome Token-based voting power

### 5. Genome Token Economy
- ERC-20 compatible token
- Rewards for data contribution
- Payment method for marketplace transactions

## 🔧 Development

### Frontend Development

```bash
cd evo2_frontend
npm run dev     # Start development server
npm run build   # Build for production
npm run lint    # Run ESLint
```

### Backend Development

```bash
cd evo2_backend
python api_server.py           # Start API server
python test_api.py            # Run API tests
python restart_server.py      # Restart server
```

### Smart Contract Development

```bash
cd contracts
npx hardhat compile           # Compile contracts
npx hardhat test             # Run tests
npx hardhat node            # Start local blockchain
```

## 🧪 Testing

### Frontend Tests
```bash
cd evo2_frontend
npm test
```

### Backend Tests
```bash
cd evo2_backend
python test_api.py
```

### Smart Contract Tests
```bash
cd contracts
npx hardhat test
```

## 🌐 Network Configuration

The platform is configured for BSC Testnet:
- **Network Name**: BSC Testnet
- **RPC URL**: https://data-seed-prebsc-1-s1.bnbchain.org:8545
- **Chain ID**: 97
- **Currency Symbol**: BNB
- **Block Explorer**: https://testnet.bscscan.com

Add BSC Testnet to MetaMask:
1. Open MetaMask
2. Go to Settings > Networks > Add Network
3. Enter the network details above

## 📖 API Documentation

### Backend API Endpoints

- `GET /` - Health check
- `POST /analyze` - Analyze genomic variants
- `GET /analysis/{analysis_id}` - Get analysis results
- Additional endpoints in `api_server.py`

### Smart Contract ABIs

Contract ABIs are available in the `contracts/artifacts/` directory after compilation.

## 🐛 Troubleshooting

### Common Issues

1. **MetaMask Connection Issues**
   - Ensure you're connected to BSC Testnet
   - Check that you have test BNB

2. **Contract Interaction Failures**
   - Verify contract addresses in `.env`
   - Ensure sufficient BNB for gas fees

3. **Backend API Errors**
   - Check if backend server is running on port 8000
   - Verify Modal.com endpoint is accessible

4. **Frontend Build Errors**
   - Clear `.next` cache: `rm -rf .next`
   - Reinstall dependencies: `rm -rf node_modules && npm install`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- [BSC Testnet Faucet](https://testnet.bnbchain.org/faucet-smart)
- [BSC Testnet Explorer](https://testnet.bscscan.com)
- [MetaMask](https://metamask.io)
- [Hardhat Documentation](https://hardhat.org/docs)
- [Next.js Documentation](https://nextjs.org/docs)

## 📞 Support

For support, please open an issue on GitHub or contact the development team.

---

Built with ❤️ for the genomics and blockchain community
