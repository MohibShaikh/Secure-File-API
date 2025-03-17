<script>
    import { auth } from '../stores/auth.js';
    import { logout } from '../stores/auth.js';
    import { navigate } from 'svelte-routing';
  </script>
  
  <nav>
    <div class="logo">
      <h1>Secure File Upload</h1>
    </div>
    <div class="links">
      {#if $auth.isAuthenticated}
        <button on:click={() => navigate('/upload')} class="btn">Upload</button>
        <button on:click={() => navigate('/files')} class="btn">Files</button>
        <button on:click={logout} class="btn">Logout</button>
      {:else}
        <button on:click={() => navigate('/login')} class="btn">Login</button>
      {/if}
    </div>
  </nav>
  
  <style>
    nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 20px;
      background-color: #2d3b45;
      color: white;
    }
  
    .logo h1 {
      margin: 0;
      font-size: 1.5rem;
    }
  
    .links {
      display: flex;
      gap: 10px;
    }
  
    .btn {
      background-color: #007BFF;
      color: white;
      padding: 10px 20px;
      border-radius: 5px;
      border: none;
      cursor: pointer;
    }
  
    .btn:hover {
      background-color: #0056b3;
    }
  </style>