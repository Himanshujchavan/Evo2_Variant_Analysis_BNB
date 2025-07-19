'use client'

import { useState } from 'react'
import { supabase } from '@/lib/supabaseClient'
import { UserProfile } from export type UserProfile = {
  id: string
  name: string
  age: number
  email: string
  mobile: string
  wallet_address: string
  nft_token_id?: string
}

export default function SignUpForm() {
  const [formData, setFormData] = useState<Omit<UserProfile, 'id'>>({
    name: '',
    age: 0,
    email: '',
    mobile: '',
    wallet_address: '',
    nft_token_id: '',
  })

  const [password, setPassword] = useState('')

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement>
  ) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    const { email } = formData

    // Step 1: Sign up user in auth
    const { data: authData, error: authError } =
      await supabase.auth.signUp({
        email,
        password,
      })

    if (authError) {
      alert(authError.message)
      return
    }

    const userId = authData?.user?.id
    if (!userId) {
      alert('User ID not returned from Supabase.')
      return
    }

    // Step 2: Insert user profile into user_profiles
    const { error: insertError } = await supabase
      .from('user_profiles')
      .insert({
        id: userId,
        ...formData,
        age: Number(formData.age),
      })

    if (insertError) {
      alert('Failed to create user profile: ' + insertError.message)
    } else {
      alert('Signup successful! Please verify your email.')
    }
  }

  return (
    <form onSubmit={handleSubmit} className="space-y-3">
      <input name="email" onChange={handleChange} placeholder="Email" required />
      <input name="password" type="password" onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
      <input name="name" onChange={handleChange} placeholder="Name" />
      <input name="age" onChange={handleChange} placeholder="Age" type="number" />
      <input name="mobile" onChange={handleChange} placeholder="Mobile" />
      <input name="wallet_address" onChange={handleChange} placeholder="Wallet Address" />
      <input name="nft_token_id" onChange={handleChange} placeholder="NFT Token ID (optional)" />
      <button type="submit">Sign Up</button>
    </form>
  )
}
