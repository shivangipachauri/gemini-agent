<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center p-6">
    <h1 class="text-4xl font-bold text-blue-600 mb-8">AI Prompt Generator</h1>

    <form @submit.prevent="submitPrompt" class="w-full max-w-xl bg-white p-6 rounded shadow">
      <input
        v-model="prompt"
        placeholder="Enter your prompt..."
        class="w-full p-3 border border-gray-300 rounded mb-4 focus:outline-none focus:ring focus:border-blue-400"
      />
      <button
        type="submit"
        class="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded w-full"
      >
        Submit
      </button>
    </form>

    <div v-if="store.history.length" class="w-full max-w-xl mt-10 space-y-4">
      <h2 class="text-2xl font-semibold text-gray-700">History</h2>
      <div
        v-for="(entry, index) in store.history"
        :key="index"
        class="bg-white p-4 rounded shadow"
      >
        <p class="text-gray-500"><strong>Prompt:</strong> {{ entry.prompt }}</p>
        <p class="text-gray-800 mt-2"><strong>Response:</strong> {{ entry.response }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { usePromptStore } from '~/stores/promptHistory.js'

const prompt = ref('')
const store = usePromptStore()

const submitPrompt = async () => {
  if (!prompt.value.trim()) return

  try {
    const res = await fetch('http://localhost:8000/api/prompt/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: prompt.value })
    })
    const data = await res.json()

    // Save to history
    store.addEntry(prompt.value, data.result)
    prompt.value = ''
  } catch (err) {
    console.error('Error:', err)
  }
}
</script>
