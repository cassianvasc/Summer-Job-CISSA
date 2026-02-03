from django.db import models
from django.contrib.auth.models import User

class Incidente(models.Model):
    usuario = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    contato_tecnico = models.CharField(max_length=255, blank=True)
    gestor_responsavel = models.CharField(max_length=255, blank=True)
    area = models.CharField(max_length=255, blank=True)

    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=50, blank=True)

    data_incidente = models.DateField(null=True, blank=True)

    equipe_seguranca = models.CharField(max_length=10, blank=True)
    descoberta = models.CharField(max_length=50, blank=True)
    categoria = models.CharField(max_length=50, blank=True)

    hosts_afetados = models.IntegerField(null=True, blank=True)
    localidade = models.CharField(max_length=50, blank=True)

    tecnologia_rede = models.CharField(max_length=50, blank=True)
    qtd_links = models.IntegerField(null=True, blank=True)

    vpn = models.CharField(max_length=50, blank=True)
    ambiente = models.CharField(max_length=50, blank=True)

    servico_afetado = models.CharField(max_length=255, blank=True)
    sistema_operacional = models.CharField(max_length=255, blank=True)
    versao = models.CharField(max_length=100, blank=True)
    ip = models.CharField(max_length=50, blank=True)

    status_incidente = models.CharField(max_length=50, blank=True)
    descricao_incidente = models.TextField()

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Incidente #{self.id} - {self.categoria}"
