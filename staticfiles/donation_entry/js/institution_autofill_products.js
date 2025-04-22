document.addEventListener('DOMContentLoaded', function () {
    console.log('📦 Produto Autofill JS carregado!');

    function bindProductChange(productSelect) {
        if (!productSelect || productSelect.dataset.bound === "true") return;

        $(productSelect).select2(); // Ativa Select2 se necessário
        productSelect.dataset.bound = "true";

        $(productSelect).on('select2:select', function (e) {
            const productID = e.params.data.id;
            if (!productID || productID === "---------") return;

            fetch(`/api/v1/product/${productID}/`)
                .then(response => response.json())
                .then(data => {
                    const row = productSelect.closest('tr');
                    const unitField = row.querySelector('[id$="-unit_quantity"]');
                    const acronymSelect = row.querySelector('[id$="-acronym"]');
                    const categorySelect = row.querySelector('[id$="-category"]');

                    if (unitField) unitField.value = data.unit_quantity || '';
                    if (acronymSelect && data.acronym) {
                        acronymSelect.value = data.acronym;
                        acronymSelect.dispatchEvent(new Event('change'));
                    }
                    if (categorySelect && data.category) {
                        categorySelect.value = data.category;
                        categorySelect.dispatchEvent(new Event('change'));
                    }
                })
                .catch(error => {
                    console.error('❌ Erro ao buscar dados do produto:', error);
                });
        });
    }

    function bindAllProductSelects() {
        document.querySelectorAll('select[id$="-item_name"]').forEach(select => {
            bindProductChange(select);
        });
    }

    // Aplica nos campos já existentes
    bindAllProductSelects();

    // 🆕 Captura quando novas linhas forem adicionadas via Django Admin inline
    document.body.addEventListener('formset:added', function (event) {
        const newRow = event.target;
        const newSelect = newRow.querySelector('select[id$="-item_name"]');
        if (newSelect) {
            console.log('🆕 Nova linha detectada. Aplicando Select2.');
            bindProductChange(newSelect);
        }
    });
});
