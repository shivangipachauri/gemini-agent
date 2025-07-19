import { defineStore } from 'pinia'
import { persistedState } from '#imports'

export const usePromptStore = defineStore('prompt', {
  state: () => ({
    history: []
  }),
  actions: {
    addEntry(prompt, response) {
      this.history.unshift({ prompt, response })
    }
  },
  persist: {
    key: 'my-prompt-history',
    storage: persistedState.localStorage   
  }
})
