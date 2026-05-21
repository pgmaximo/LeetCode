class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Retorna os índices de dois números em `nums` que somam `target`.

        Estratégia:
        - Percorrer a lista uma única vez.
        - Para cada número atual, calcular o complemento.
        - Verificar se esse complemento já apareceu antes.
        - Guardar cada número visitado em um dicionário.
        """

        # Dicionário no formato:
        # número -> índice
        seen = {}

        # Percorre cada número da lista junto com seu índice.
        for i, n in enumerate(nums):

            # Calcula o número que falta para chegar no target.
            # Exemplo: target = 9, n = 7, diff = 2.
            diff = target - n

            # Se o complemento já foi visto antes,
            # então encontramos os dois números que somam target.
            if diff in seen:
                return [seen[diff], i]

            # Caso contrário, guardamos o número atual
            # para que ele possa ser usado nas próximas iterações.
            seen[n] = i

        # Retorno de segurança.
        return []