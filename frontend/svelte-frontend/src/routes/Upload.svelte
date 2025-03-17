<script>
    import { auth, refreshToken } from '../stores/auth.js';
  
    let file = null; // To store the selected file
    let errorMessage = ''; // To store error messages
  
    const handleFileUpload = async () => {
      if (!file) {
        errorMessage = 'Please select a file to upload.';
        return;
      }
  
      // Log the file to verify it's being captured correctly
      console.log('Selected file:', file);
  
      const formData = new FormData();
      formData.append('file', file); // Append the file to FormData
  
      // Log FormData entries to verify the file is appended correctly
      for (let [key, value] of formData.entries()) {
        console.log(key, value);
      }
  
      try {
        const response = await fetch('http://localhost:8000/api/files/upload_file/', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${$auth.accessToken}`,
          },
          body: formData,
        });
  
        if (response.ok) {
          alert('File uploaded successfully!');
          errorMessage = ''; // Clear any previous error message
        } else {
          const error = await response.json();
          errorMessage = error.error || 'File upload failed.';
        }
      } catch (error) {
        errorMessage = 'An error occurred while uploading the file.';
        console.error(error);
      }
    };
  </script>
  
  <main>
    <h2>Upload a File</h2>
  
    <!-- Bind to a single file instead of a FileList -->
    <input type="file" bind:files={file} on:change={(e) => (file = e.target.files[0])} />
    <button on:click={handleFileUpload}>Upload</button>
  
    {#if errorMessage}
      <p style="color: red;">{errorMessage}</p>
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
    }
  
    h2 {
      text-align: center;
      color: #333;
    }
  
    input[type="file"] {
      margin: 10px 0;
    }
  
    button {
      background-color: #007BFF;
      color: white;
      padding: 10px 20px;
      border-radius: 5px;
      border: none;
      cursor: pointer;
    }
  
    button:hover {
      background-color: #0056b3;
    }
  
    p {
      color: red;
      text-align: center;
    }
  </style>