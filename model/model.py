from httpx import AsyncClient
from jinja2 import Template

class Model:

    async def get_modules(self):
        async with AsyncClient() as client:
            response = await client.get(f'http://cademi.us-3.evennode.com/get/modules-aulas')
            modules_data = response.json()

            template_str = """
                <header class="squeezhead">
                    <p> {{ title }} </p>
                </header>
                <div class="squeezecnt">
                    <p>
                        {% for aula in aulas %}
                            <span class="aula" id="{{ aula[1] }}">{{ aula[0] }}</span>
                        {% endfor %}
                    </p>
                </div>
            """
            template = Template(template_str)

            modules_html = []

            for module in modules_data['binary']:
                title = module['module_title']
                aulas = module['aulas']

                module_html = template.render(title=title, aulas=aulas)
                modules_html.append(module_html)

            return "\n".join(modules_html)

    async def get_video(self, id):
        async with AsyncClient() as client:
            response = await client.get(f'http://cademi.us-3.evennode.com/get/videos/{id}')
            return response.json()