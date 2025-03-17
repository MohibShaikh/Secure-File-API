<script>
	import { Router, Route, Link, navigate } from 'svelte-routing';  // Import from svelte-routing
	import { auth } from './stores/auth.js';  // Correct import path for auth store
  
	// Import the components for file upload, viewing files, and login
	import Upload from './routes/Upload.svelte';
	import Files from './routes/Files.svelte';
	import Login from './routes/Login.svelte';
  
	// Function to handle logout
	const logout = () => {
	  localStorage.removeItem("access_token");
	  localStorage.removeItem("refresh_token");
	  auth.set({ accessToken: null, refreshToken: null, isAuthenticated: false });
	  navigate('/login'); // Redirect to login page after logout
	};
  </script>
  
  <Router>
	<header class="header">
	  <nav class="navbar">
		<div class="logo">
		  <h2>Secure File Upload</h2>
		</div>
		<div class="navbar-links">
		  {#if $auth.isAuthenticated}
			<button class="nav-btn" on:click={logout}>Logout</button>
		  {:else}
			<Link to="/login" class="nav-btn">Login</Link>
		  {/if}
		</div>
	  </nav>
	</header>
  
	<div class="container">
	  <h1>Welcome to Secure File Management</h1>
	  <p>Upload and manage your encrypted files securely</p>
	  
	  <div class="action-buttons">
		{#if $auth.isAuthenticated}
		  <button class="btn" on:click={() => navigate('/upload')}>Upload File</button>
		  <button class="btn" on:click={() => navigate('/files')}>View Files</button>
		{:else}
		  <Link to="/login" class="btn">Login to Access</Link>
		{/if}
	  </div>
	</div>
  
	<!-- Define the routes -->
	<Route path="/upload">
	  <Upload />
	</Route>
  
	<Route path="/files">
	  <Files />
	</Route>
  
	<Route path="/login">
	  <Login /> <!-- Add the Login component here -->
	</Route>
  </Router>
  
  <style>
	/* Style remains the same as before */
	* {
	  margin: 0;
	  padding: 0;
	  box-sizing: border-box;
	}
  
	body {
	  font-family: 'Arial', sans-serif;
	  background-color: #f4f7fc;
	  color: #333;
	}
  
	main {
	  display: flex;
	  flex-direction: column;
	  align-items: center;
	  justify-content: center;
	  min-height: 100vh;
	  padding: 20px;
	  background-color: #f4f7fc;
	}
  
	h1 {
	  font-size: 2.5rem;
	  color: #2d3b45;
	  text-align: center;
	  margin-bottom: 10px;
	}
  
	p {
	  font-size: 1.2rem;
	  color: #444;
	  margin-bottom: 20px;
	  text-align: center;
	}
  
	.action-buttons {
	  display: flex;
	  gap: 20px;
	  flex-wrap: wrap;
	  justify-content: center;
	}
  
	.btn {
	  background-color: #007BFF;
	  color: white;
	  padding: 12px 20px;
	  border-radius: 5px;
	  border: none;
	  cursor: pointer;
	  font-size: 1.1rem;
	  transition: background-color 0.3s ease;
	}
  
	.btn:hover {
	  background-color: #0056b3;
	}
  
	.navbar {
	  display: flex;
	  justify-content: space-between;
	  align-items: center;
	  width: 100%;
	  padding: 15px 30px;
	  background-color: #2d3b45;
	  color: white;
	}
  
	.navbar .logo h2 {
	  font-size: 1.5rem;
	  color: #fff;
	}
  
	.navbar-links {
	  display: flex;
	  gap: 20px;
	}
  
	.nav-btn {
	  background-color: #28a745;
	  color: white;
	  padding: 10px 20px;
	  border-radius: 5px;
	  border: none;
	  cursor: pointer;
	  font-size: 1.1rem;
	  transition: background-color 0.3s ease;
	}
  
	.nav-btn:hover {
	  background-color: #218838;
	}
  
	/* Container for Main Content */
	.container {
	  width: 100%;
	  max-width: 900px;
	  padding: 20px;
	  background-color: white;
	  border-radius: 8px;
	  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	  margin-top: 30px;
	  text-align: center;
	}
  
	/* Responsive Design */
	@media (max-width: 768px) {
	  .navbar {
		flex-direction: column;
		gap: 10px;
		text-align: center;
	  }
  
	  .navbar-links {
		justify-content: center;
		width: 100%;
	  }
  
	  .action-buttons {
		flex-direction: column;
	  }
  
	  h1 {
		font-size: 2rem;
	  }
	}
  
	@media (max-width: 480px) {
	  .btn {
		padding: 10px 15px;
	  }
  
	  h1 {
		font-size: 1.5rem;
	  }
	}
  </style>