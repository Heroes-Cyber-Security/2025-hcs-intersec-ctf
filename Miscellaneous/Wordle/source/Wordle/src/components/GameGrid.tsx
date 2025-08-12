'use client';

import { useState, useEffect } from 'react';

interface GameGridProps {
  guesses: string[];
  currentGuess: string;
  targetWord: string;
  maxAttempts: number;
  wordLength: number;
}

interface TileProps {
  letter: string;
  status: 'correct' | 'present' | 'absent' | 'empty';
  isAnimating?: boolean;
  delay?: number;
}

function Tile({ letter, status, isAnimating = false, delay = 0 }: TileProps) {
  const [showFlip, setShowFlip] = useState(false);

  useEffect(() => {
    if (isAnimating) {
      const timer = setTimeout(() => {
        setShowFlip(true);
      }, delay);
      return () => clearTimeout(timer);
    } else {
      setShowFlip(false);
    }
  }, [isAnimating, delay]);

  const getStatusClasses = () => {
    if (!showFlip && isAnimating) return 'bg-gray-700 border-gray-600 text-gray-300';
    
    switch (status) {
      case 'correct': return 'bg-green-500 border-green-500 text-white';
      case 'present': return 'bg-yellow-500 border-yellow-500 text-white';
      case 'absent': return 'bg-gray-600 border-gray-600 text-white';
      default: return letter ? 'bg-gray-700 border-gray-500 text-white' : 'bg-gray-800 border-gray-600 text-gray-400';
    }
  };

  return (
    <div 
      className={`
        w-14 h-14 border-2 flex items-center justify-center text-xl font-bold uppercase
        transition-all duration-500 transform rounded-md
        ${getStatusClasses()}
        ${showFlip && isAnimating ? 'animate-flip' : ''}
      `}
    >
      {letter}
    </div>
  );
}

export default function GameGrid({ guesses, currentGuess, targetWord, maxAttempts, wordLength }: GameGridProps) {
  const [animatingRow, setAnimatingRow] = useState<number | null>(null);
  const [prevGuessesLength, setPrevGuessesLength] = useState(0);

  useEffect(() => {
    if (guesses.length > prevGuessesLength) {
      setAnimatingRow(guesses.length - 1);
      const timer = setTimeout(() => {
        setAnimatingRow(null);
      }, wordLength * 200 + 800);
      setPrevGuessesLength(guesses.length);
      return () => clearTimeout(timer);
    }
  }, [guesses.length, wordLength, prevGuessesLength]);

  const getLetterStatus = (guess: string, index: number): 'correct' | 'present' | 'absent' => {
    const letter = guess[index];
    const targetLetter = targetWord[index];
    
    if (letter === targetLetter) {
      return 'correct';
    }
    
    const targetLetterCount = targetWord.split('').filter(l => l === letter).length;
    const correctPositionsCount = guess.split('').filter((l, i) => l === letter && targetWord[i] === letter).length;
    
    let presentCount = 0;
    for (let i = 0; i <= index; i++) {
      if (guess[i] === letter && targetWord[i] !== letter) {
        presentCount++;
      }
    }
    
    const availableForPresent = targetLetterCount - correctPositionsCount;
    
    if (presentCount <= availableForPresent && targetWord.includes(letter)) {
      return 'present';
    }
    
    return 'absent';
  };

  return (
    <div className="grid grid-rows-6 gap-y-2 mb-8 justify-items-center">
      {Array.from({ length: maxAttempts }).map((_, rowIndex) => (
        <div key={rowIndex} className="grid grid-cols-5 gap-x-px w-full justify-items-center">
          {Array.from({ length: wordLength }).map((_, colIndex) => {
            let letter = '';
            let status: 'correct' | 'present' | 'absent' | 'empty' = 'empty';
            let isAnimating = false;

            if (rowIndex < guesses.length) {
              letter = guesses[rowIndex][colIndex] || '';
              status = letter ? getLetterStatus(guesses[rowIndex], colIndex) : 'empty';
              isAnimating = animatingRow === rowIndex;
            } else if (rowIndex === guesses.length) {
              letter = currentGuess[colIndex] || '';
            }

            return (
              <Tile
                key={colIndex}
                letter={letter}
                status={status}
                isAnimating={isAnimating}
                delay={colIndex * 200}
              />
            );
          })}
        </div>
      ))}
    </div>
  );
}
