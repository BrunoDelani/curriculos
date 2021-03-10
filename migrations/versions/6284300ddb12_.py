"""empty message

Revision ID: 6284300ddb12
Revises: 
Create Date: 2021-03-10 16:52:57.930051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6284300ddb12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instituicoes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=False),
    sa.Column('sigla', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('senha', sa.String(length=200), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usuarios_email'), 'usuarios', ['email'], unique=True)
    op.create_table('atuacoes_profissionais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('instituicao_id', sa.Integer(), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['instituicao_id'], ['instituicoes.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cursos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=False),
    sa.Column('instituicao_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['instituicao_id'], ['instituicoes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('formacoes_complementares',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('instituicao_id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=200), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['instituicao_id'], ['instituicoes.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('atividades_profissionais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('atuacao_profissional_id', sa.Integer(), nullable=False),
    sa.Column('descricao', sa.String(length=200), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['atuacao_profissional_id'], ['atuacoes_profissionais.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('formacoes_academicas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('usuario_id', sa.Integer(), nullable=False),
    sa.Column('curso_id', sa.Integer(), nullable=False),
    sa.Column('trabalho_conclusao', sa.String(length=200), nullable=False),
    sa.Column('inicio', sa.Date(), nullable=False),
    sa.Column('termino', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['curso_id'], ['cursos.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuarios.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('formacoes_academicas')
    op.drop_table('atividades_profissionais')
    op.drop_table('formacoes_complementares')
    op.drop_table('cursos')
    op.drop_table('atuacoes_profissionais')
    op.drop_index(op.f('ix_usuarios_email'), table_name='usuarios')
    op.drop_table('usuarios')
    op.drop_table('instituicoes')
    # ### end Alembic commands ###
