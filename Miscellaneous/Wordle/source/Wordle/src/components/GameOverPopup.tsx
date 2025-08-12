'use client';

interface GameOverPopupProps {
  targetWord: string;
  onClose: () => void;
}

export default function GameOverPopup({ targetWord, onClose }: GameOverPopupProps) {
  const handleBackdropClick = (e: React.MouseEvent) => {
    if (e.target === e.currentTarget) {
      onClose();
    }
  };

  return (
    <div 
      className="fixed inset-0 bg-black bg-opacity-70 backdrop-blur-sm flex items-center justify-center z-50"
      onClick={handleBackdropClick}
    >
      <div className="bg-gray-800 rounded-xl p-8 max-w-md w-full mx-4 shadow-2xl animate-scale-in border border-gray-700">
        <div className="text-center">
          <h2 className="text-3xl font-bold text-red-400 mb-4">💀 Game Over!</h2>
          <p className="text-gray-300 mb-4">You&apos;ve used all 6 attempts.</p>
          <p className="text-gray-300 mb-6">The word was:</p>
          <div className="bg-gray-900 p-4 rounded-lg mb-6 border border-gray-600">
            <code className="text-2xl font-bold font-mono text-green-400">{targetWord}</code>
          </div>
          <p className="text-sm text-gray-400">Click anywhere to play again</p>
        </div>
      </div>
    </div>
  );
}
