import { writable, get } from "svelte/store";
import { navigate } from 'svelte-routing';

// Store for holding authentication data
export const auth = writable({
    accessToken: localStorage.getItem("access_token"),
    refreshToken: localStorage.getItem("refresh_token"),
    isAuthenticated: false
});

// Function to check if a token is expired
export const isTokenExpired = (token) => {
    if (!token) return true;
    const payload = JSON.parse(atob(token.split('.')[1])); // Decode the token payload
    return payload.exp * 1000 < Date.now(); // Check if the token is expired
};

// Function to login a user
export const login = async (username, password) => {
    try {
        const response = await fetch('http://localhost:8000/api/token/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('access_token', data.access);
            localStorage.setItem('refresh_token', data.refresh);
            auth.set({
                accessToken: data.access,
                refreshToken: data.refresh,
                isAuthenticated: true
            });
            return { success: true }; // Success
        } else {
            const error = await response.json();
            return { success: false, error: error.detail || "Authentication failed" }; // Failure
        }
    } catch (error) {
        console.error(error);
        return { success: false, error: "Network error" }; // Network failure
    }
};

// Function to log the user out
export const logout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    auth.set({ accessToken: null, refreshToken: null, isAuthenticated: false });
    navigate('/login'); // Redirect to login page
};

// Function to refresh the access token
export const refreshToken = async () => {
    const refresh_token = localStorage.getItem('refresh_token');
    
    if (!refresh_token) {
        logout();  // No refresh token means user is logged out
        return;
    }

    const response = await fetch('http://localhost:8000/api/token/refresh/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh: refresh_token })
    });

    if (response.ok) {
        const data = await response.json();
        localStorage.setItem('access_token', data.access);
        auth.update(store => ({
            ...store,
            accessToken: data.access
        }));
    } else {
        logout();  // Refresh token is invalid, log the user out
    }
};

// Function to handle requests with authentication
export const fetchWithAuth = async (url, options = {}) => {
    let token = get(auth).accessToken;

    if (!token || isTokenExpired(token)) {
        await refreshToken(); // Refresh token if expired or missing
        token = get(auth).accessToken; // Get the new token
    }

    // Add Authorization header with access token
    options.headers = {
        ...options.headers,
        'Authorization': `Bearer ${token}`,
    };

    // Make the request
    let response = await fetch(url, options);

    // If the response is Unauthorized (401), try refreshing the token and retry the request
    if (response.status === 401) {
        await refreshToken();  // Refresh token if expired
        response = await fetch(url, options);  // Retry the request with the new token
    }

    return response;
};

// Auto login on page load if access token is available
if (get(auth).accessToken) {
    auth.set({ ...get(auth), isAuthenticated: true });
}