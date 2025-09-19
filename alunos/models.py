from django.db import models

class Aluno(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    TURNO_CHOICES = [
        ('M', 'Manhã'),
        ('T', 'Tarde'),
        ('N', 'Noite'),
    ]

    nome_completo = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    telefone_emergencia = models.CharField(max_length=15, blank=True, null=True)

    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    numero_matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    serie_ano = models.CharField(max_length=20)
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome_completo
