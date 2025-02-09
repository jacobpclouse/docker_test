<template>
  <div>
    <form @submit.prevent="sendMessage">
      <input type="text" v-model="message">
      <button type="submit">Send</button>
    </form>

    <!-- Displaying the response from the backend -->
    <div v-if="responseMessage">
      <p>Response: {{ responseMessage }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '',
      responseMessage: ''  // Store the response from the backend
    };
  },
  methods: {
    sendMessage() {
      axios.post('http://127.0.0.1:5000/message', { message: this.message })
        .then(response => {
          this.responseMessage = response.data;  // Save the response to be displayed
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
