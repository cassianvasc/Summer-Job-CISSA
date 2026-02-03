from django.contrib import admin
from .models import Incidente


@admin.register(Incidente)
class IncidenteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "categoria",
        "status_incidente",
        "usuario",
        "data_incidente",
        "criado_em",
    )

    list_filter = (
        "categoria",
        "status_incidente",
        "localidade",
        "ambiente",
        "criado_em",
    )

    search_fields = (
        "descricao_incidente",
        "ip",
        "servico_afetado",
        "email",
        "contato_tecnico",
    )

    ordering = ("-criado_em",)

    readonly_fields = ("criado_em",)

    fieldsets = (
        ("Responsáveis", {
            "fields": (
                "usuario",
                "contato_tecnico",
                "gestor_responsavel",
                "area",
            )
        }),

        ("Contato", {
            "fields": (
                "email",
                "telefone",
            )
        }),

        ("Classificação do Incidente", {
            "fields": (
                "categoria",
                "status_incidente",
                "descoberta",
                "equipe_seguranca",
            )
        }),

        ("Impacto", {
            "fields": (
                "hosts_afetados",
                "localidade",
            )
        }),

        ("Infraestrutura", {
            "fields": (
                "tecnologia_rede",
                "qtd_links",
                "vpn",
                "ambiente",
            )
        }),

        ("Sistema Afetado", {
            "fields": (
                "servico_afetado",
                "sistema_operacional",
                "versao",
                "ip",
            )
        }),

        ("Descrição do Incidente", {
            "fields": (
                "descricao_incidente",
            )
        }),

        ("Registro", {
            "fields": (
                "data_incidente",
                "criado_em",
            )
        }),
    )
