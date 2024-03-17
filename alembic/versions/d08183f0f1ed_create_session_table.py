from sqlalchemy.engine.reflection import Inspector
from alembic import op
import sqlalchemy as sa


revision: str = 'd08183f0f1ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    inspector = Inspector.from_engine(op.get_bind())
    tables = inspector.get_table_names()

    if 'sessions' not in tables:
        op.create_table(
            'sessions',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('result', sa.Integer, nullable=True),
            sa.Column('status', sa.String, nullable=False),
        )

def downgrade():
    op.drop_table('sessions')
