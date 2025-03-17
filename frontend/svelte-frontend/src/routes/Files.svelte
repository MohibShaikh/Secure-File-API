<script>
  import { auth } from '../stores/auth.js';
  import { onMount } from 'svelte';

  let files = [];
  let errorMessage = '';

  // Fetch the list of files when the component mounts
  onMount(async () => {
    try {
      const response = await fetch('http://localhost:8000/api/files/', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${$auth.accessToken}`,
        },
      });

      if (response.ok) {
        files = await response.json();
      } else {
        errorMessage = 'Failed to load files. Please try again.';
        console.error("Failed to load files:", await response.text());
      }
    } catch (error) {
      errorMessage = 'An error occurred while fetching files.';
      console.error("Error fetching files:", error);
    }
  });

  // Download a file by making a GET request
  const downloadFile = async (fileId, fileName) => {
    try {
      const response = await fetch(`http://localhost:8000/api/files/${fileId}/download/`, {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${$auth.accessToken}`,
        },
      });

      if (response.ok) {
        const blob = await response.blob(); // Get the file blob
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = fileName || 'download'; // Use original file name or fallback
        link.click();
      } else {
        errorMessage = 'Failed to download file. Please try again.';
        console.error("Failed to download file:", await response.text());
      }
    } catch (error) {
      errorMessage = 'An error occurred while downloading the file.';
      console.error("Error downloading file:", error);
    }
  };
</script>

<style>
  .file-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
  }

  .file-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    border: 1px solid #ccc;
    margin: 10px 0;
    background-color: #f9f9f9;
    border-radius: 5px;
  }

  .file-item button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 3px;
  }

  .file-item button:hover {
    background-color: #0056b3;
  }

  .file-name {
    font-weight: bold;
    color: #333;
  }

  .file-size {
    color: #666;
  }

  .error {
    color: red;
    margin-top: 10px;
  }
</style>

<div>
  <h2>Your Uploaded Files</h2>
  {#if files.length > 0}
    <ul class="file-list">
      {#each files as file}
        <li class="file-item">
          <div>
            <div class="file-name">{file.name}</div>
            <div class="file-size">{(file.size / 1024).toFixed(2)} KB</div>
          </div>
          <button on:click={() => downloadFile(file.id, file.name)}>Download</button>
        </li>
      {/each}
    </ul>
  {:else}
    <p>No files uploaded yet.</p>
  {/if}

  {#if errorMessage}
    <p class="error">{errorMessage}</p>
  {/if}
</div>