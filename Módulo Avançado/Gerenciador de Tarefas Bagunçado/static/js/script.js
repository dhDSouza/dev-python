document.addEventListener('DOMContentLoaded', () => {
    // Função para adicionar tarefa
    document.getElementById('tarefaForm').addEventListener('submit', function (event) {
        event.preventDefault();
        const titulo = document.getElementById('titulo').value;
        if (titulo) {
            fetch('/tarefas', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ titulo: titulo })
            })
                .then(response => response.json())
                .then(data => {
                    if (data.mensagem) {
                        location.reload(); // Recarrega a página após adicionar a tarefa
                    }
                });
        }
    });

    // Função para deletar tarefa
    document.querySelectorAll('.btn-deletar').forEach(button => {
        button.addEventListener('click', function () {
            const tarefaId = this.closest('li').getAttribute('data-id');
            fetch(`/tarefas/${tarefaId}`, { method: 'DELETE' })
                .then(response => response.json())
                .then(data => {
                    if (data.mensagem) {
                        this.closest('li').remove(); // Remove o item da lista
                    }
                });
        });
    });
})