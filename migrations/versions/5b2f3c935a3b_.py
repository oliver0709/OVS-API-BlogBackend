"""empty message

Revision ID: 5b2f3c935a3b
Revises: 
Create Date: 2024-10-14 19:54:21.440426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b2f3c935a3b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('blog_status', sa.String(length=50), nullable=False),
    sa.Column('featured_image_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog')
    # ### end Alembic commands ###
