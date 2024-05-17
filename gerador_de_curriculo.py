from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Thiago Alexsandro Bianchi de Souza', 0, 1, 'C')
        self.set_font('Arial', '', 10)
        self.cell(0, 10, '(11) 98812-4773 | Thiago-hiago201@hotmail.com', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 10)
        self.multi_cell(0, 10, body)
        self.ln()

pdf = PDF()
pdf.add_page()

# Objetivo
pdf.chapter_title('Objetivo')
objetivo = (
    "Contribuir para a sustentação de ambientes com foco em MongoDB, aplicando meus conhecimentos "
    "em instalação, configuração, suporte e migração de bancos de dados, visando a eficiência e a performance do sistema."
)
pdf.chapter_body(objetivo)

# Experiência Profissional
pdf.chapter_title('Experiência Profissional')

experiencias = [
    ("Analista Computacional - Tecnocomp LTDA", "16/05/2023 - Atual",
     "- Automação de processos utilizando Python (bibliotecas Selenium, Pandas, Pynput)\n"
     "- Manutenção e suporte de VMs e servidores\n"
     "- Manutenção de hardware e software\n"
     "- Gestão de sistemas Windows e pacotes Office"),

    ("Estágio - Desenvolvedor - Nerus", "17/06/2021 - 22/09/2022",
     "- Automação de processos em Excel e Google Sheets\n"
     "- Desenvolvimento de automações web com Python\n"
     "- Uso do Power BI para visualização de dados"),

    ("Analista de Dados - Luana Tavares", "21/12/2021 - 10/07/2022",
     "- Desenvolvimento de planos estratégicos em redes com Excel e Google Data Studio\n"
     "- Automação web utilizando Python"),

    ("Estagiário de Help Desk - Câmara Municipal dos Vereadores", "24/09/2020 – 31/12/2020",
     "- Suporte técnico N1 e N2"),

    ("Estagiário de Help Desk - Liberty Parking", "02/2019 – 12/2019",
     "- Suporte técnico N1 e N2"),
]

for title, date, desc in experiencias:
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 10, f'{title} ({date})', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 10, desc)
    pdf.ln()

# Habilidades Técnicas
pdf.chapter_title('Habilidades Técnicas')
habilidades = (
    "- Bancos de Dados: MongoDB, MySQL, PostgreSQL\n"
    "- Sistemas Operacionais: Red Hat Enterprise Linux (RHEL), Windows Server\n"
    "- Cloud e Ferramentas: Google Cloud, Mongo Atlas\n"
    "- Automação e Scripting: Python, Shell Script, Ansible, Terraform\n"
    "- Desenvolvimento Web: HTML, JavaScript\n"
    "- Outros: Power BI, Pacote Office, Excel Avançado, Google Analytics"
)
pdf.chapter_body(habilidades)

# Formação Acadêmica
pdf.chapter_title('Formação Acadêmica')
formacao = (
    "- Engenharia da Computação (Conclusão em 06/2024)"
)
pdf.chapter_body(formacao)

# Certificações e Cursos
pdf.chapter_title('Certificações e Cursos')

cursos = (
    "- Python: \n"
    "  - Mundo 1, 2, 3 Python 3 – Curso em Vídeo - 120H\n"
    "  - Curso de Python 3 do Básico Ao Avançado - Udemy - 141H\n"
    "  - Formação Python Developer – DIO – 64H\n"
    "- Ciência de Dados: Potência Tech powered by iFood | Ciência de Dados – DIO – 80H (em andamento)\n"
    "- Database: Database Experience - DIO - 54H\n"
    "- Programação: Potência Tech iFood - Programação do Zero - DIO - 68H\n"
    "- Outros: Web Design, Desenvolvimento Web com PHP, Banco de Dados MySQL, Contabilidade Tributária"
)
pdf.chapter_body(cursos)

# Idiomas
pdf.chapter_title('Idiomas')
idiomas = (
    "- Inglês: Intermediário"
)
pdf.chapter_body(idiomas)

# Save PDF
pdf_output = "Curriculo_Thiago_Alexsandro_Bianchi_de_Souza.pdf"
pdf.output(pdf_output)

print(f"PDF gerado com sucesso: {pdf_output}")
