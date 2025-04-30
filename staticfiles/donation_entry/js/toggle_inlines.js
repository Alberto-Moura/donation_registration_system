document.addEventListener('DOMContentLoaded', function () {
    function bindTypeDonationChange() {
        const typeDonationSelect = document.getElementById('id_type_donation');
        if (!typeDonationSelect) {
            return;
        }

        function removerInlinesPorHref(href) {
            const tabId = href.replace('#', '');
            const tab = document.getElementById(tabId);
            if (!tab) return;
        
            const botoesRemover = tab.querySelectorAll('.inline-deletelink');
            botoesRemover.forEach(botao => botao.click());
        }
        

        function toggleTabs(value) {
            const itensDoadosTab = document.getElementById('itens-doados-tab');
            const itensDescartadosTab = document.getElementById('itens-descartados-tab');
            const itensDoadosButton = document.querySelector('a[href="#itens-doados-tab"]')?.parentElement;
            const itensDescartadosButton = document.querySelector('a[href="#itens-descartados-tab"]')?.parentElement;

            if (!itensDoadosTab || !itensDescartadosTab || !itensDoadosButton || !itensDescartadosButton) {
                return;
            }

            if (value === 'DESCARTE') {
                removerInlinesPorHref('#itens-doados-tab');
                itensDoadosTab.style.display = 'none';
                itensDoadosButton.style.display = 'none';
                itensDescartadosTab.style.display = 'block';
                itensDescartadosButton.style.display = 'block';
            } else if (value === 'INVENTÁRIO') {
                removerInlinesPorHref('#itens-descartados-tab');
                itensDoadosTab.style.display = 'block';
                itensDoadosButton.style.display = 'block';
                itensDescartadosTab.style.display = 'none';
                itensDescartadosButton.style.display = 'none';
            } else {
                itensDoadosTab.style.display = '';
                itensDoadosButton.style.display = '';
                itensDescartadosTab.style.display = '';
                itensDescartadosButton.style.display = '';
            }
        }

        // Evento para mudança manual
        $(typeDonationSelect).on('select2:select', function (e) {
            toggleTabs(e.params.data.id);
        });
        
        // Dispara ao carregar
        toggleTabs(typeDonationSelect.value);
    }

    const observer = new MutationObserver(() => {
        const select = document.getElementById('id_type_donation');
        if (select) {
            bindTypeDonationChange();
            observer.disconnect();
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
});
