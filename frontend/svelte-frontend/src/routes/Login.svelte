<script>
    import { login } from '../stores/auth.js'; // Import the login function from auth store
    import { navigate } from 'svelte-routing'; // Import navigate for redirection
  
    let username = ''; // Bind to the username input
    let password = ''; // Bind to the password input
    let errorMessage = ''; // Store error messages for display
  
    // Function to handle login
    const handleLogin = async () => {
      if (!username || !password) {
        errorMessage = 'Please enter both username and password.';
        return;
      }
  
      // Call the login function from auth.js
      const result = await login(username, password);
  
      if (result.success) {
        errorMessage = ''; // Clear any previous error message
        navigate('/upload'); // Redirect to the upload page after successful login
      } else {
        errorMessage = result.error || 'Authentication failed. Please try again.'; // Show error message
      }
    };
  </script>
  
  <main>
    <h1>Login</h1>
  
    <!-- Login Form -->
    <form on:submit|preventDefault={handleLogin} class="login-form">
      <label for="username">Username</label>
      <input
        type="text"
        id="username"
        bind:value={username}
        placeholder="Enter your username"
        class="input"
      />
  
      <label for="password">Password</label>
      <input
        type="password"
        id="password"
        bind:value={password}
        placeholder="Enter your password"
        class="input"
      />
  
      <button type="submit" class="btn">Login</button>
    </form>
  
    <!-- Display error message if any -->
    {#if errorMessage}
      <p class="error">{errorMessage}</p>
    {/if}
  
    <!-- Link to register or other pages (optional) -->
    <p>
    </p>
  </main>
  
  <style>
    main {
      font-family: 'Arial', sans-serif;
      background-color: #f9f9f9;
      padding: 40px 20px;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      max-width: 400px;
      margin: 20px auto;
      text-align: center;
    }
  
    h1 {
      color: #2d3b45;
      margin-bottom: 20px;
    }
  
    .login-form {
      display: flex;
      flex-direction: column;
      gap: 15px;
    }
  
    .input {
      padding: 10px;
      border-radius: 5px;
      border: 1px solid #ccc;
      font-size: 1rem;
    }
  
    .btn {
      background-color: #007BFF;
      color: white;
      padding: 10px 20px;
      border-radius: 5px;
      border: none;
      cursor: pointer;
      font-size: 1rem;
      transition: background-color 0.3s ease;
    }
  
    .btn:hover {
      background-color: #0056b3;
    }
  
    .error {
      color: red;
      margin-top: 10px;
    }
  </style>