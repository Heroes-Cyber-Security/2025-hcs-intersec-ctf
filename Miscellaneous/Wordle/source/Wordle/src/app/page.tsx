'use client';

import WordleGame from '@/components/WordleGame';

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-900 flex items-center justify-center p-4">
      <WordleGame />
    </div>
  );
}
