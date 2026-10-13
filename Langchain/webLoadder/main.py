from langchain_community.document_loaders import WebBaseLoader
import bs4

loader = WebBaseLoader(web_path=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
                       bs_kwargs={
                           'parse_only':bs4.SoupStrainer(
                               class_=('post-title','post-content','post-header')
                           )
                           
                       },
                       )

documents = loader.load()
print(documents)
#print(documents[0].page_content)


#top > main > article > div.post-content > p.h