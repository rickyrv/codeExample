const request = require('request');
const moment = require('moment')
const cheerio = require('cheerio');
const insertArticles = require('../insertArticles');

const hemptoday = async () => {
    const domain = 'https://hemptoday.net/';
    return new Promise(async (res, rej) => {
        request(domain, async function (error, response, html) {
            if (!error && response.statusCode == 200) {
                var $ = cheerio.load(html);
                var articles = [];
                $('article').each(function (i, element) {
                    var a = $(element).find('.entry-title.content-list-title  a');
                    var title = a.text();
                    var link = a.attr('href');
                    var content = $(element)
                        .find('.content-list-excerpt')
                        .text();
                    var date = $(element)
                        .find('.entry-meta-date')
                        .text();

                    var dateFormatted = moment(date, 'MMMM D, YYYY').format();
                    articles.push({
                        title: title,
                        link: link,
                        content: content,
                        date: dateFormatted,
                        domain: domain
                    });
                });
                console.log('news hemptoday europa start');
                await insertArticles(articles);
                console.log('news hemptoday europa completed ');
                res(true);
            } else {
                console.log('error request hemptoday europa');
                rej(error);
            }
        });
    });
};

module.exports = hemptoday
