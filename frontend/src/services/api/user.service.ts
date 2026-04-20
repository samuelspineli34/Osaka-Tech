// frontend/src/services/api/user.service.ts
import { apiClient } from './api-client';
import { User } from '../../interfaces/user.interface';

export const userService = {
    async getAllUsers() {
        return await apiClient.get<User[]>('/user');
    },
    async getUserById(id: string) {
        return await apiClient.get<User>(`/user/${id}`);
    },
    async createUser(user: Omit<User, 'id'>) {
        return await apiClient.post('/user', user);
    },
    async updateUser(id: string, user: Omit<User, 'id'>) {
        return await apiClient.put(`/user/${id}`, user);
    },
    async deleteUser(id: string) {
        return await apiClient.delete(`/user/${id}`);
    }
};