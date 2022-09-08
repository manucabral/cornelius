---
title: Development Team
---

<script setup>
    import { VPTeamMembers } from 'vitepress/theme'
    const members = [
        {
            avatar: 'https://avatars.githubusercontent.com/u/83357673?v=4',
            name: 'Manuel Cabral',
            title: 'CEO & Development',
            links: [
                { icon: 'github', link: 'https://www.github.com/manucabral' },
            ]
        },
        {
            avatar: 'https://avatars.githubusercontent.com/u/101936353?v=4',
            name: 'Leo Araya',
            title: 'Development & Tester',
            orgLink: 'https://leoarayav.herokuapp.com',
            links: [
                { icon: 'github', link: 'https://www.github.com/leoarayav' }
            ],
        }
    ]
</script>

<div align="center">
    <h1>Cornelius official development team</h1>
    <VPTeamMembers size="small" :members="members"/>
</div>