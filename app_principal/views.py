from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages   # 👈 ADICIONADO
from .models import Incidente


@login_required
def home(request):
    return render(request, 'app_principal/homehtml.html')


@login_required
def denuncia(request):
    if request.method == "POST":
        Incidente.objects.create(
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

        messages.success(request, "Incidente registrado com sucesso.")

        return redirect("home")

    return render(request, 'app_principal/denuncia.html')
