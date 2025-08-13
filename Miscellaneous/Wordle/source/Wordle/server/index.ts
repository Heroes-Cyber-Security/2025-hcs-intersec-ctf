import { serve } from "bun";

const PORT = parseInt(process.env.BACKEND_PORT || "3001");
const FLAG = process.env.FLAG || "FLAG{congrats_you_solved_intersec_wordle_challenge}";
const DICTIONARY_API_URL = process.env.DICTIONARY_API_URL || "https://api.dictionaryapi.dev/api/v2/entries/en";
const RANDOM_WORD_API_URL = process.env.RANDOM_WORD_API_URL || "https://random-word-api.vercel.app/api?words=1&length=5";

const isValidWord = async (word: string): Promise<boolean> => {
  try {
    const response = await fetch(`${DICTIONARY_API_URL}/${word.toLowerCase()}`);
    return response.ok;
  } catch (error) {
    return false;
  }
};

const getRandomWord = async (): Promise<string> => {
  try {
    const response = await fetch(RANDOM_WORD_API_URL);
    const words = await response.json();
    return words[0].toUpperCase();
  } catch (error) {
    return "SMILE";
  }
};

serve({
  port: PORT,
  async fetch(req) {
    const url = new URL(req.url);
    const corsHeaders = {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    };

    if (req.method === "OPTIONS") {
      return new Response(null, { headers: corsHeaders });
    }

    if (url.pathname === "/api/word") {
      const word = await getRandomWord();
      return Response.json({ word }, { headers: corsHeaders });
    }

    if (url.pathname === "/api/validate") {
      const { word } = await req.json();
      const isValid = await isValidWord(word);
      return Response.json({ isValid }, { headers: corsHeaders });
    }

    if (url.pathname === "/api/flag") {
      return Response.json({ flag: FLAG }, { headers: corsHeaders });
    }

    return new Response("Not Found", { status: 404, headers: corsHeaders });
  },
});

console.log(`Bun server running on http://localhost:${PORT}`);
