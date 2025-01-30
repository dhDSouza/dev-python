from app.controllers.controllers import app
from app.models.models import criar_tabela

criar_tabela()
app.run(debug=True)