import { supabase } from '@/lib/supabaseClient'
import { UserProfile } from '@/types/user'

export const fetchUserProfile = async (): Promise<UserProfile | null> => {
  const {
    data: { user },
    error: userError,
  } = await supabase.auth.getUser()

  if (userError || !user) return null

  const { data, error } = await supabase
    .from('user_profiles')
    .select('*')
    .eq('id', user.id)
    .single()

  if (error) {
    console.error('Error fetching profile:', error)
    return null
  }

  return data as UserProfile
}
