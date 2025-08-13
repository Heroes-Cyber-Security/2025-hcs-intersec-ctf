'use client';

interface PopupProps {
  message: string;
}

export default function Popup({ message }: PopupProps) {
  return (
    <div className="fixed top-20 left-1/2 transform -translate-x-1/2 z-50">
      <div className="bg-red-600 text-white px-6 py-3 rounded-lg shadow-xl animate-fade-in border border-red-500">
        <span className="font-semibold">{message}</span>
      </div>
    </div>
  );
}
