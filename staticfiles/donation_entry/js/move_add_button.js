document.addEventListener("DOMContentLoaded", function () {
    const interval = setInterval(() => {
        document.querySelectorAll('.inline-group .tabular').forEach((table) => {
            const addRowTr = table.querySelector('tr.add-row');
            if (addRowTr) {
                const addButton = addRowTr.querySelector('a');
                if (addButton) {
                    const wrapper = document.createElement('div');
                    wrapper.classList.add('custom-add-button');
                    wrapper.style.marginTop = "15px";
                    wrapper.style.textAlign = "left";

                    wrapper.appendChild(addButton);
                    table.parentNode.insertBefore(wrapper, table.nextSibling);
                    addRowTr.remove();
                }
            }
        });

        // Quando terminar de processar todos, limpa o intervalo
        if (document.querySelectorAll('.inline-group .tabular tr.add-row').length === 0) {
            clearInterval(interval);
        }
    }, 100); // tenta a cada 100ms até funcionar
});
