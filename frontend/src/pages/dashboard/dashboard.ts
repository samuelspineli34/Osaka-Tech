import { initSidebar } from '../../components/sidebar';
import { userService } from '../../services/api/user.service';
import { ticketService } from '../../services/api/ticket.service';

async function updateStats() {
    const userStat = document.getElementById('stat-users');
    const ticketStat = document.getElementById('stat-tickets');

    // Carregar Usuários
    try {
        const users = await userService.getAllUsers();
        if (userStat) userStat.textContent = users.length.toString();
    } catch (error) {
        console.error("Error fetching users:", error);
    }

    // Carregar Tickets (vai dar erro até você criar a rota, mas não trava o de cima)
    try {
        const tickets = await ticketService.getAllTickets();
        if (ticketStat) ticketStat.textContent = tickets.length.toString();
    } catch (error) {
        console.warn("Tickets API not ready yet");
    }
}

document.addEventListener('DOMContentLoaded', () => {
    initSidebar();
    updateStats();
});