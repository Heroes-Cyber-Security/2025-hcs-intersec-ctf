'use client';

import { useState, useEffect, useCallback } from 'react';
import GameGrid from './GameGrid';
import Keyboard from './Keyboard';
import Popup from './Popup';
import FlagPopup from './FlagPopup';
import GameOverPopup from './GameOverPopup';

const MAX_ATTEMPTS = 6;
const WORD_LENGTH = 5;
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:50032';

export default function WordleGame() {
  const [targetWord, setTargetWord] = useState('');
  const [guesses, setGuesses] = useState<string[]>([]);
  const [currentGuess, setCurrentGuess] = useState('');
  const [gameStatus, setGameStatus] = useState<'playing' | 'won' | 'lost'>('playing');
  const [showInvalidWord, setShowInvalidWord] = useState(false);
  const [showFlag, setShowFlag] = useState(false);
  const [flag, setFlag] = useState('');
  const [isLoading, setIsLoading] = useState(true);
  const [showGameOver, setShowGameOver] = useState(false);

  const fetchNewWord = useCallback(async () => {
    try {
      setIsLoading(true);
      const response = await fetch(`${API_URL}/api/word`);
      const data = await response.json();
      setTargetWord(data.word);
    } catch {
      setTargetWord('SMILE');
    } finally {
      setIsLoading(false);
    }
  }, []);

  const resetGame = useCallback(() => {
    setGuesses([]);
    setCurrentGuess('');
    setGameStatus('playing');
    setShowInvalidWord(false);
    setShowFlag(false);
    setShowGameOver(false);
    fetchNewWord();
  }, [fetchNewWord]);

  useEffect(() => {
    fetchNewWord();
  }, [fetchNewWord]);

  const validateWord = async (word: string): Promise<boolean> => {
    try {
      const response = await fetch(`${API_URL}/api/validate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ word })
      });
      const data = await response.json();
      return data.isValid;
    } catch {
      return false;
    }
  };

  const fetchFlag = async () => {
    try {
      const response = await fetch(`${API_URL}/api/flag`);
      const data = await response.json();
      setFlag(data.flag);
    } catch {
      setFlag('error_fetching_flag');
    }
  };

  const handleKeyPress = useCallback(async (key: string) => {
    if (gameStatus !== 'playing' || isLoading) return;

    if (key === 'ENTER') {
      if (currentGuess.length !== WORD_LENGTH) return;
      
      const isValid = await validateWord(currentGuess);
      
      if (!isValid) {
        setShowInvalidWord(true);
        setTimeout(() => setShowInvalidWord(false), 2000);
        return;
      }

      const newGuesses = [...guesses, currentGuess];
      setGuesses(newGuesses);
      setCurrentGuess('');

      if (currentGuess === targetWord) {
        setGameStatus('won');
        await fetchFlag();
        setShowFlag(true);
      } else if (newGuesses.length >= MAX_ATTEMPTS) {
        setGameStatus('lost');
        setShowGameOver(true);
      }
    } else if (key === 'BACKSPACE') {
      setCurrentGuess(prev => prev.slice(0, -1));
    } else if (currentGuess.length < WORD_LENGTH && /^[A-Z]$/.test(key)) {
      setCurrentGuess(prev => prev + key);
    }
  }, [gameStatus, currentGuess, guesses, targetWord, isLoading]);

  const handleFlagClose = () => {
    setShowFlag(false);
    setTimeout(() => {
      resetGame();
    }, 100);
  };

  const handleGameOverClose = () => {
    setShowGameOver(false);
    setTimeout(() => {
      resetGame();
    }, 100);
  };

  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      event.preventDefault();
      const key = event.key.toUpperCase();
      
      if (key === 'ENTER' || key === 'BACKSPACE') {
        handleKeyPress(key);
      } else if (key.length === 1 && /^[A-Z]$/.test(key)) {
        handleKeyPress(key);
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleKeyPress]);

  if (isLoading) {
    return (
      <div className="w-full max-w-lg mx-auto bg-gray-800 rounded-2xl shadow-2xl p-8 border border-gray-700">
        <h1 className="text-4xl font-bold text-center mb-8 text-white">
          Intersec-Wordle
        </h1>
        <div className="flex justify-center items-center h-64">
          <div className="text-xl text-gray-300 animate-pulse">Loading new word...</div>
        </div>
      </div>
    );
  }

  return (
    <div className="w-full max-w-lg mx-auto bg-gray-800 rounded-2xl shadow-2xl p-8 border border-gray-700">
      <h1 className="text-4xl font-bold text-center mb-8 text-white">
        Intersec-Wordle
      </h1>
      
      <GameGrid
        guesses={guesses}
        currentGuess={currentGuess}
        targetWord={targetWord}
        maxAttempts={MAX_ATTEMPTS}
        wordLength={WORD_LENGTH}
      />
      
      <Keyboard onKeyPress={handleKeyPress} guesses={guesses} targetWord={targetWord} />
      
      {showInvalidWord && (
        <Popup message="Not a valid word!" />
      )}
      
      {showFlag && (
        <FlagPopup flag={flag} onClose={handleFlagClose} />
      )}
      
      {showGameOver && (
        <GameOverPopup targetWord={targetWord} onClose={handleGameOverClose} />
      )}
    </div>
  );
}
