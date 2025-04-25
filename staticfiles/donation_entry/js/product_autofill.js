document.addEventListener('DOMContentLoaded', function () {
    console.log('✅ JS de produto carregado');

    function bindProductAutofill(row) {
        const select = row.querySelector('[name$="-item_name"]');
        if (!select) {
            console.warn('⚠️ Campo item_name não encontrado na linha:', row);
            return;
        }

        // Inicializa Select2 (caso ainda não esteja ativado)
        if (!$(select).hasClass("select2-hidden-accessible")) {
            $(select).select2();
        }

        // Usa select2:select para pegar ID corretamente
        $(select).on('select2:select', function (e) {
            const productId = e.params.data.id;
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

    // Aplica para novas linhas
    document.addEventListener('formset:added', function (event) {
        bindProductAutofill(event.detail.form);
    });
});
