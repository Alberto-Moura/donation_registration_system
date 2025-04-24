document.addEventListener("DOMContentLoaded", function () {
    const interval = setInterval(() => {
        const addRowTr = document.querySelector('.inline-group .tabular tr.add-row');
        const table = document.querySelector('.inline-group .tabular');

        if (addRowTr && table) {
            // Move o conteúdo do <td> (botão) para fora da tabela
            const addButton = addRowTr.querySelector('a');
            const wrapper = document.createElement('div');

            wrapper.classList.add('custom-add-button');
            wrapper.style.marginTop = "15px";
            wrapper.style.textAlign = "left";  // ou "right" se quiser à direita

            wrapper.appendChild(addButton);
            table.parentNode.insertBefore(wrapper, table.nextSibling);

            // Remove a <tr> que estava na tabela
            addRowTr.remove();

            clearInterval(interval); // Para de tentar mover
        }
    }, 100); // tenta mover a cada 100ms até funcionar
});
