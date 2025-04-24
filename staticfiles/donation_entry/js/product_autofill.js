document.addEventListener('DOMContentLoaded', function () {
    console.log('✅ JS de produto carregado');

    function bindProductAutofill(row) {
        console.log('🆕 Nova linha detectada. Aplicando Select2.');
        const select = row.querySelector('select[id$="-item_name"]');
        if (!select) return;

        console.log('Não achou o select')
        // Inicializa Select2 (caso não esteja ativado ainda)
        if (!$(select).hasClass("select2-hidden-accessible")) {
            $(select).select2();
        }

        // Escuta o evento correto
        $(select).on('select2:select', function (e) {
            const productId = e.params.data.id;
            console.log('📦 Buscando produto...');
            if (!productId) return;

            fetch(`/api/v1/product/${productId}/`)
                .then(res => res.json())
                .then(data => {
                    const acronymP = row.querySelector('.field-product_acronym p');
                    const categoryP = row.querySelector('.field-product_category p');

                    if (acronymP) acronymP.textContent = data.acronym || '-';
                    if (categoryP) categoryP.textContent = data.category || '-';
                })
                .catch(err => {
                    console.error('❌ Erro ao buscar produto:', err);
                });
        });
    }

    // Aplica nas linhas existentes
    document.querySelectorAll('tr.dynamic-donated_items').forEach(bindProductAutofill);

    // Nova linha inline
    document.addEventListener('formset:added', function (event) {
        bindProductAutofill(event.detail.form);
    });
});
