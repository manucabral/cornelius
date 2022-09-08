const docsSidebar = [
    {
        text: 'Introduction',
        collapsible: true,
        items: [
            { text: 'What is cornelius?', link: '/guide/what-is-cornelius' },
            { text: 'Get started', link: '/guide/get-started' }
        ]
    },
    {
        text: 'Classes',
        collapsible: true,
        items: [
            { text: 'Cursor', link: '/class/cursor' },
            { text: 'Keyboard', link: '/class/keyboard' }
        ]
    }
]

export default {
    title: 'cornelius',
    markdown: 
    {
        lineNumbers: true
    },
    themeConfig: 
    {
        siteTitle: 'Cornelius',
        logo: './img/cornelius.png',
        footer: {
            message: 'Cornelius Official Website',
            copyright: 'Copyright © 2022 - All rights reserved'
        },
        nav: 
        [
            { text: 'Home', link: '/' },
            { text: 'Team', link: '/team'},
            { text: 'Docs', link: '/guide/what-is-cornelius' }
        ],
        sidebar: {
            '/guide/': docsSidebar,
            '/class/': docsSidebar
        }
    }
}
