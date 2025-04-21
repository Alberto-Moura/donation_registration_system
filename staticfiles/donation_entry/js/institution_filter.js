document.addEventListener('DOMContentLoaded', function () {
    console.log('📦 institution_filter.js carregado!');

    function bindInstitutionFilter() {
        const typeSelect = document.getElementById('id_typesInstitution');
        const nameSelect = document.getElementById('id_name');

        if (!typeSelect || !nameSelect) {
            console.warn('❗ Campos não encontrados ainda.');
            return;
        }

        console.log('✅ Campos prontos.');

        // Ativa Select2 para os dois campos
        $(typeSelect).select2();
        $(nameSelect).select2();

        // Evento do Select2 para tipo de instituição
        $(typeSelect).on('select2:select', function (e) {
            const typeId = e.params.data.id;
            console.log("📌 Tipo selecionado:", typeId);
        
            $(nameSelect).empty().trigger('change');
        
            if (!typeId) return;
        
            fetch(`/api/v1/institution/type/${typeId}/`)
                .then(response => response.json())
                .then(data => {
                    // 1️⃣ Adiciona opção vazia padrão
                    $(nameSelect).append(new Option("---------", "", true, true));
        
                    // 2️⃣ Adiciona instituições retornadas
                    const options = data.result.map(inst => {
                        return new Option(inst.name, inst.id, false, false);
                    });
        
                    $(nameSelect).append(options).trigger('change');
                })
                .catch(err => {
                    console.error('❌ Erro ao buscar instituições:', err);
                });
        });
    }

    // Verifica se os campos já existem
    if (document.getElementById('id_typesInstitution') && document.getElementById('id_name')) {
        bindInstitutionFilter();
        return;
    }

    // Ativa observer caso os campos ainda não existam
    const observer = new MutationObserver(() => {
        const typeField = document.getElementById('id_typesInstitution');
        const nameField = document.getElementById('id_name');
        if (typeField && nameField) {
            bindInstitutionFilter();
            observer.disconnect();
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
});
