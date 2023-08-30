export const metadata = {
  title: 'Home - HaX',
  description: 'HaX offers a suite of robust features designed to achieve optimal and impactful results',
}

import Banner from '@/components/banner'
import Features from '@/components/features'

export default function Home() {
  return (
    <>
      <Banner />
      <Features />
    </>
  )
}
