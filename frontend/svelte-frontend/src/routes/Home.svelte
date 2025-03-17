<script>
    import { auth } from '../stores/auth.js';
    import { navigate } from 'svelte-routing';
  </script>
  
  <main>
    <h1>Welcome to Secure File Management</h1>
    <p>Upload and manage your encrypted files securely.</p>
  
    {#if $auth.isAuthenticated}
      <button on:click={() => navigate('/upload')} class="btn">Upload File</button>
      <button on:click={() => navigate('/files')} class="btn">View Files</button>
    {:else}
      <button on:click={() => navigate('/login')} class="btn">Login to Access</button>
    {/if}
  </main>
  
  <style>
    main {
      font-family: 'Arial', sans-serif;
      background-color: #f9f9f9;
      padding: 40px 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      max-width: 600px;
      margin: 20px auto;
      text-align: center;
    }
  
    h1 {
      color: #333;
    }
  
    .btn {
      background-color: #007BFF;
      color: white;
      padding: 10px 20px;
      border-radius: 5px;
      border: none;
      cursor: pointer;
      margin: 10px;
    }
  
    .btn:hover {
      background-color: #0056b3;
    }
  </style>