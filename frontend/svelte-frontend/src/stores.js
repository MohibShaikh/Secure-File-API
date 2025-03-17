import { writable } from "svelte/store";

export const auth = writable({
    accessToken: localStorage.getItem("access_token"),
    refreshToken: localStorage.getItem("refresh_token"),
    isAuthenticated: false
});

export const login = async (username, password) => {
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
    } else {
        console.log("Authentication failed");
    }
};

export const logout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    auth.set({ accessToken: null, refreshToken: null, isAuthenticated: false });
};
