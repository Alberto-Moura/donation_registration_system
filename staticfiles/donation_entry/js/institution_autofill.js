document.addEventListener('DOMContentLoaded', function () {
    function bindInstitutionChange() {
        const institutionSelect = document.getElementById('id_name');
        if (!institutionSelect) {
            return;
        }

        $(institutionSelect).on('select2:select', function (e) {
            const institutionID = e.params.data.id;

            if (!institutionID || institutionID === "---------") {
                return;
            }

            fetch(`/api/v1/institution/${institutionID}/`)
                .then(response => {
                    if (!response.ok) throw new Error("Erro na requisição");
                    return response.json();
                })
                .then(data => {
                    document.getElementById('id_address').value = data.address || '';
                    document.getElementById('id_number').value = data.number || '';
                    document.getElementById('id_phone').value = data.phone || '';
                    document.getElementById('id_contact').value = data.contact || '';
                    if (data.neighborhood) {
                        const neighborhoodSelect = document.getElementById('id_neighborhood');
                        if (neighborhoodSelect) {
                            neighborhoodSelect.value = data.neighborhood;
                            neighborhoodSelect.dispatchEvent(new Event('change'));
                        }
                    }
                })
                .catch(error => {
                    console.error('Erro ao buscar dados da instituição:', error);
                });
        });
    }

    const observer = new MutationObserver(() => {
        const select = document.getElementById('id_name');
        if (select) {
            bindInstitutionChange();
            observer.disconnect();
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
});
