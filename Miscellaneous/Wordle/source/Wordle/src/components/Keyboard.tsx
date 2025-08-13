'use client';

interface KeyboardProps {
  onKeyPress: (key: string) => void;
  guesses: string[];
  targetWord: string;
}

const KEYBOARD_ROWS = [
  ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
  ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
  ['ENTER', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'BACKSPACE']
];

export default function Keyboard({ onKeyPress, guesses, targetWord }: KeyboardProps) {
  const getKeyStatus = (key: string): 'correct' | 'present' | 'absent' | 'unused' => {
    if (key === 'ENTER' || key === 'BACKSPACE') return 'unused';
    
    let hasCorrect = false;
    let hasPresent = false;
    let hasAbsent = false;
    
    for (const guess of guesses) {
      for (let i = 0; i < guess.length; i++) {
        if (guess[i] === key) {
          if (targetWord[i] === key) {
            hasCorrect = true;
          } else if (targetWord.includes(key)) {
            const targetCount = targetWord.split('').filter(l => l === key).length;
            const correctCount = guess.split('').filter((l, idx) => l === key && targetWord[idx] === key).length;
            
            let presentCount = 0;
            for (let j = 0; j <= i; j++) {
              if (guess[j] === key && targetWord[j] !== key) {
                presentCount++;
              }
            }
            
            if (presentCount <= targetCount - correctCount) {
              hasPresent = true;
            } else {
              hasAbsent = true;
            }
          } else {
            hasAbsent = true;
          }
        }
      }
    }
    
    if (hasCorrect) return 'correct';
    if (hasPresent) return 'present';
    if (hasAbsent) return 'absent';
    return 'unused';
  };

  const getKeyClasses = (key: string) => {
    const status = getKeyStatus(key);
    const baseClasses = 'font-bold text-sm rounded-md transition-all duration-200 hover:bg-opacity-80';
    
    if (key === 'ENTER' || key === 'BACKSPACE') {
      return `${baseClasses} px-3 py-4 bg-gray-600 text-gray-200 text-xs hover:bg-gray-500`;
    }
    
    const statusClasses = {
      correct: 'bg-green-500 text-white hover:bg-green-400',
      present: 'bg-yellow-500 text-white hover:bg-yellow-400',
      absent: 'bg-gray-600 text-white hover:bg-gray-500',
      unused: 'bg-gray-700 text-gray-200 hover:bg-gray-600 border border-gray-600'
    };
    
    return `${baseClasses} px-4 py-4 ${statusClasses[status]}`;
  };

  return (
    <div className="space-y-3">
      {KEYBOARD_ROWS.map((row, rowIndex) => (
        <div key={rowIndex} className="flex justify-center gap-1.5">
          {row.map((key) => (
            <button
              key={key}
              onClick={() => onKeyPress(key)}
              className={getKeyClasses(key)}
            >
              {key === 'BACKSPACE' ? '←' : key}
            </button>
          ))}
        </div>
      ))}
    </div>
  );
}
