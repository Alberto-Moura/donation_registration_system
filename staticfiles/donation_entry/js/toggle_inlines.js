document.addEventListener('DOMContentLoaded', function() {
    const typeDonationField = document.getElementById('id_type_donation');

    function toggleTabs() {
        const itensDoadosTab = document.getElementById('itens-doados-tab');
        const itensDescartadosTab = document.getElementById('itens-descartados-tab');

        const itensDoadosButton = document.querySelector('a[href="#itens-doados-tab"]').parentElement;
        const itensDescartadosButton = document.querySelector('a[href="#itens-descartados-tab"]').parentElement;

        if (!typeDonationField || !itensDoadosTab || !itensDescartadosTab || !itensDoadosButton || !itensDescartadosButton) {
            return;
        }

        if (typeDonationField.value === 'DESCARTE') {
            // Esconde aba e conteúdo de "Itens Doados", mostra "Itens descartados"
            itensDoadosTab.style.display = 'none';
            itensDoadosButton.style.display = 'none';
            itensDescartadosTab.style.display = 'block';
            itensDescartadosButton.style.display = 'block';
        } else if (typeDonationField.value === 'INVENTÁRIO') {
            // Esconde aba e conteúdo de "Itens descartados", mostra "Itens Doados"
            itensDoadosTab.style.display = 'block';
            itensDoadosButton.style.display = 'block';
            itensDescartadosTab.style.display = 'none';
            itensDescartadosButton.style.display = 'none';
        } else {
            // Em outros casos, mostra tudo
            itensDoadosTab.style.display = 'block';
            itensDoadosButton.style.display = 'block';
            itensDescartadosTab.style.display = 'block';
            itensDescartadosButton.style.display = 'block';
        }
    }

    typeDonationField.addEventListener('change', toggleTabs);

    toggleTabs();  // Executa ao carregar a página
});
