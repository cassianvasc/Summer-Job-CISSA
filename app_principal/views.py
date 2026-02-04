from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Incidente
from .API import registrar_incidente


@login_required
def home(request):
    return render(request, 'app_principal/homehtml.html')


@login_required
def denuncia(request):

    if request.method == "POST":

        incidente = Incidente.objects.create(
            usuario=request.user,

            contato_tecnico=request.POST.get("contato_tecnico"),
            gestor_responsavel=request.POST.get("gestor_responsavel"),
            area=request.POST.get("area"),

            email=request.POST.get("email"),
            telefone=request.POST.get("telefone"),

            data_incidente=request.POST.get("data_incidente") or None,

            equipe_seguranca=request.POST.get("equipe_seguranca"),
            descoberta=request.POST.get("descoberta"),
            categoria=request.POST.get("categoria"),

            hosts_afetados=request.POST.get("hosts_afetados") or None,
            localidade=request.POST.get("localidade"),

            tecnologia_rede=request.POST.get("tecnologia_rede"),
            qtd_links=request.POST.get("qtd_links") or None,

            vpn=request.POST.get("vpn"),
            ambiente=request.POST.get("ambiente"),

            servico_afetado=request.POST.get("servico_afetado"),
            sistema_operacional=request.POST.get("sistema_operacional"),
            versao=request.POST.get("versao"),
            ip=request.POST.get("ip"),

            status_incidente=request.POST.get("status_incidente"),
            descricao_incidente=request.POST.get("descricao_incidente"),
        )

        dados_blockchain = {
            "usuario": request.user.username,

            "contato_tecnico": incidente.contato_tecnico,
            "gestor_responsavel": incidente.gestor_responsavel,
            "area": incidente.area,

            "email": incidente.email,
            "telefone": incidente.telefone,
            "data_incidente": str(incidente.data_incidente),

            "equipe_seguranca": incidente.equipe_seguranca,
            "descoberta": incidente.descoberta,
            "categoria": incidente.categoria,

            "hosts_afetados": incidente.hosts_afetados,
            "localidade": incidente.localidade,

            "tecnologia_rede": incidente.tecnologia_rede,
            "qtd_links": incidente.qtd_links,
            "vpn": incidente.vpn,
            "ambiente": incidente.ambiente,

            "servico_afetado": incidente.servico_afetado,
            "sistema_operacional": incidente.sistema_operacional,
            "versao": incidente.versao,
            "ip": incidente.ip,

            "status_incidente": incidente.status_incidente,
            "descricao_incidente": incidente.descricao_incidente,
        }

        registrar_incidente(dados_blockchain)

        messages.success(request, "Incidente registrado com sucesso.")
        return redirect("home")

    return render(request, 'app_principal/denuncia.html')
