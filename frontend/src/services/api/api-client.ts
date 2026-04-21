const envUrl = import.meta.env.VITE_API_URL || 'http://localhost:5000';

// Garantimos que a BASE_URL sempre termine com /api
const BASE_URL = envUrl.endsWith('/api') ? envUrl : `${envUrl}/api`;

const getHeaders = (): HeadersInit => {
    const token = localStorage.getItem('token');
    const headers: HeadersInit = {
        'Content-Type': 'application/json'
    };
    if (token) {
        headers['Authorization'] = `Bearer ${token}`;
    }
    return headers;
};

const handleResponse = async (response: Response) => {
    if (response.status === 401) {
        // Se NÃO estiver na página de login, aí sim é sessão expirada
        if (!window.location.pathname.includes('login')) {
            localStorage.clear();
            window.location.href = '/login';
            throw new Error('Session expired');
        }
        // Se estiver no login, o erro é apenas credenciais inválidas
        throw new Error('Invalid email or password');
    }
    
    if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.error || 'Server error');
    }
    return await response.json();
};

export const apiClient = {
    async get<T>(endpoint: string): Promise<T> {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
            headers: getHeaders()
        });
        return await handleResponse(response);
    },

    async post<T>(endpoint: string, data: any): Promise<T> {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
            method: 'POST',
            headers: getHeaders(),
            body: JSON.stringify(data)
        });
        return await handleResponse(response);
    },

    async put<T>(endpoint: string, data: any): Promise<T> {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
            method: 'PUT',
            headers: getHeaders(),
            body: JSON.stringify(data)
        });
        return await handleResponse(response);
    },

    async delete<T>(endpoint: string): Promise<T> {
        const response = await fetch(`${BASE_URL}${endpoint}`, {
            method: 'DELETE',
            headers: getHeaders()
        });
        return await handleResponse(response);
    }
};