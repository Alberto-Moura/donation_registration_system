document.addEventListener('DOMContentLoaded', function () {
    console.log("📦 JS de auto-preenchimento carregado!");

    function bindInstitutionChange() {
        const institutionSelect = document.getElementById('id_name');
        console.log("📦 Campo institutionSelect encontrado:", institutionSelect);

        if (!institutionSelect) {
            console.warn("❗ Campo 'id_name' não encontrado.");
            return;
        }

        // Usar evento do Select2!
        $(institutionSelect).on('select2:select', function (e) {
            console.warn("✅ Evento select2:select disparado.");
            const institutionID = e.params.data.id;
            console.log("🔎 ID selecionado:", institutionID);

            if (!institutionID || institutionID === "---------") {
                console.warn("⚠️ Nenhuma instituição válida selecionada.");
                return;
            }

            fetch(`/api/v1/institution/${institutionID}/`)
                .then(response => {
                    if (!response.ok) throw new Error("Erro na requisição");
                    return response.json();
                })
                .then(data => {
                    console.log("✅ Dados recebidos:", data);
                    document.getElementById('id_address').value = data.address || '';
                    document.getElementById('id_number').value = data.number || '';
                    document.getElementById('id_phone').value = data.phone || '';
                    document.getElementById('id_contact').value = data.contact || '';
                    if (data.neighborhood) {
                        const neighborhoodSelect = document.getElementById('id_neighborhood');
                        if (neighborhoodSelect) {
                            console.log("🏘️ Bairro selecionado:", data.neighborhood);
                            neighborhoodSelect.value = data.neighborhood;
                            neighborhoodSelect.dispatchEvent(new Event('change'));
                        }
                    }
                })
                .catch(error => {
                    console.error('❌ Erro ao buscar dados da instituição:', error);
                });
        });
    }

    const observer = new MutationObserver(() => {
        const select = document.getElementById('id_name');
        if (select) {
            bindInstitutionChange();
            console.log("✅ Evento conectado ao campo com Select2.");
            observer.disconnect();
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
});
