<script setup>
import { ref } from 'vue'
import { usePromptHistory } from '~/stores/promptHistory.js'

const userInput = ref('')
const { prompts, addPrompt } = usePromptHistory()

const submitPrompt = () => {
  if (userInput.value.trim()) {
    addPrompt(userInput.value)
    userInput.value = ''
  }
}
</script>

<template>
  <div class="p-6">
    <input
      v-model="userInput"
      type="text"
      class="border p-2 rounded w-full"
      placeholder="Type your prompt..."
    />
    <button
      class="mt-2 bg-blue-500 text-white px-4 py-2 rounded"
      @click="submitPrompt"
    >
      Submit
    </button>

    <div class="mt-4">
      <h2 class="font-bold mb-2">Prompt History:</h2>
      <ul class="list-disc list-inside">
        <li v-for="prompt in prompts" :key="prompt.id">{{ prompt.text }}</li>
      </ul>
    </div>
  </div>
</template>
