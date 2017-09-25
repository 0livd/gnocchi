# Copyright 2017 The Gnocchi Developers
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""Use an id as primary key for archive policy

Revision ID: 71cfe62bcf98
Revises: 1e1a63d3d186
Create Date: 2017-09-24 19:46:22.660503

"""

import uuid
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '71cfe62bcf98'
down_revision = '1e1a63d3d186'
branch_labels = None
depends_on = None

archive_policy_rule = sa.Table(
    'archive_policy',
    sa.MetaData(),
    sa.Column('name', sa.String(length=255), nullable=False, unique=True),
)


def upgrade():
    op.add_column('archive_policy',
                  sa.Column('id',
                            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
                            nullable=False))
    op.add_column('metric',
                  sa.Column('archive_policy_id',
                            sqlalchemy_utils.types.uuid.UUIDType(binary=False),
                            nullable=False))
    op.drop_constraint('name', 'archive_policy_rule', type_='primary')
    op.create_unique_constraint('archive_policy_rule_name_unique', 'archive_policy_rule', ['name'])
    op.create_index('archive_policy_name_unique', 'archive_policy', ['name'], unique=True)
